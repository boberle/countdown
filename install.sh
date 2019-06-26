name=countdown
mainscript=countdown-1.2.0.py

libdest=~/prog/lib/$name
bindest=~/prog/bin/$name

if [ ! -x "$libdest" ]; then
	mkdir $libdest
fi
cp -t $libdest \
   $mainscript

cat << EOF > $bindest
#!/bin/bash
python3 $libdest/$mainscript "\$@"
EOF

chmod u+x $bindest
