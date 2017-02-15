# Reiniciador de la base de datos
# Reemplazen el nombre de usuario
# Ejecuten haciendo [sh resetdb.sh] en consola
sudo -u postgres psql -c 'DROP DATABASE skywalker;'
sudo -u postgres psql -c 'CREATE DATABASE skywalker WITH OWNER postgres;'
sudo -u postgres psql -c 'GRANT ALL PRIVILEGES ON DATABASE skywalker TO postgres;'
