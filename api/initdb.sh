#!/bin/sh
MYSQL=$@
echo "CREATE DATABASE IF NOT EXISTS \`${MYSQL_DATABASE}_test\`;" | ${MYSQL}
echo "GRANT ALL PRIVILEGES ON  \`${MYSQL_DATABASE}_test\` . * TO  '${MYSQL_USER}'@'%';" | ${MYSQL}
