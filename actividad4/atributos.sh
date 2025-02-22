
archivo="$1"
permisos=$(stat -c "%a"  "$archivo")
usuario=$(stat -c "%U" "$archivo")
grupo=$(stat -c "%G" "$archivo")
tamano=$(stat -c "%s" "$archivo")
fecha=$(stat -c "%y" "$archivo")
nombre=$(basename "$archivo")

echo > atributosinfo.txt

echo "Permisos: $permisos"
echo "Usuario: $usuario"
echo "Grupo $grupo"
echo "Tamaño $tamano bytes"
echo "Fecha y Hora: $fecha"
echo "Nombre del Archivo: $nombre"
echo "Información guardada en atributos.info.txt"

echo "Diego David Estrada Domínguez - al03110'270 - $(dates +%F)"


