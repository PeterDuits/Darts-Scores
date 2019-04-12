import os


def from_environment():
    return {
        'env': os.getenv('ENV', 'dev'),
        'local': os.getenv('LOCAL') == 'true',
        'secret': os.getenv('SECRET', 'localdevsecret'),
        'jwt_encryption_algorithm': os.getenv('JWT_ENCRYPTION_ALGORITHM'),
        'database': {
            'connection': os.getenv('DB_CONNECTION', 'default'),
            'connections': {
                'default': {
                    'host': os.getenv('DB_HOST', 'db'),
                    'port': os.getenv('DB_PORT', '3306'),
                    'database': os.getenv('DB_NAME', 'api'),
                    'username': os.getenv('DB_USERNAME', 'test'),
                    'password': os.getenv('DB_PASSWORD', 'testpass')
                },
                'test': {
                    'host': os.getenv('DB_HOST', 'db'),
                    'port': os.getenv('DB_PORT', '3306'),
                    'database': os.getenv('TEST_DB_NAME', 'api_test'),
                    'username': os.getenv('DB_USERNAME', 'test'),
                    'password': os.getenv('DB_PASSWORD', 'testpass')
                }
            }
        }
    }
