# Modern zeroconf implementation for Python 3
# Replaces pybonjour which is not Python 3 compatible

__all__ = ["Zeroconf"]

import logging

logger = logging.getLogger(__name__)


class Zeroconf(object):
    """A simple class to publish a network service with zeroconf using
    the modern zeroconf library (Python 3 compatible).
    """

    def __init__(self, name, port, **kwargs):
        self.name = name
        self.port = port
        self.stype = kwargs.get('stype', "_http._tcp.local.")
        self.server = None
        self.info = None
        
        # Make sure stype ends with .local.
        if not self.stype.endswith('.local.'):
            if self.stype.endswith('.'):
                self.stype = self.stype[:-1] + '.local.'
            else:
                self.stype = self.stype + '.local.'

    def publish(self):
        try:
            from zeroconf import ServiceInfo, Zeroconf as ZC
            import socket
            
            # Get local IP address
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            
            # Create TXT record for DAAP
            txt_record = {
                'txtvers': '1',
                'iTSh Version': '131073',
                'Machine Name': self.name,
                'Password': '0',
            }
            
            # Convert IP to bytes
            ip_bytes = socket.inet_aton(local_ip)
            
            # Create service info
            service_name = f"{self.name}.{self.stype}"
            
            self.info = ServiceInfo(
                self.stype,
                service_name,
                port=self.port,
                properties=txt_record,
                addresses=[ip_bytes],
                server=f"{hostname}.local."
            )
            
            # Create and register service
            self.server = ZC()
            self.server.register_service(self.info)
            
            logger.info(f'Published DAAP service: {service_name} on port {self.port}')
            
        except ImportError:
            logger.warning('zeroconf library not found, cannot announce presence')
            logger.warning('Install with: pip install zeroconf')
            self.server = None
        except Exception as e:
            logger.error(f'Failed to publish zeroconf service: {e}')
            self.server = None

    def unpublish(self):
        if self.server is not None and self.info is not None:
            try:
                self.server.unregister_service(self.info)
                self.server.close()
                logger.info('Unpublished DAAP service')
            except Exception as e:
                logger.error(f'Failed to unpublish zeroconf service: {e}')
