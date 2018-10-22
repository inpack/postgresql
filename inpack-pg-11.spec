[project]
name = postgresql11
version = 11.0
vendor = postgresql.org
homepage = https://www.postgresql.org
groups = dev/db
description = advanced open source database

%build

cd {{.inpack__pack_dir}}/deps

if [ ! -f "postgresql-{{.project__version}}.tar.bz2" ]; then
    wget https://ftp.postgresql.org/pub/source/v{{.project__version}}/postgresql-{{.project__version}}.tar.bz2
fi
if [ ! -d "postgresql-{{.project__version}}" ]; then
    tar -vxjf postgresql-{{.project__version}}.tar.bz2
fi


mkdir -p {{.buildroot}}/{bin,data,lib,share}

cd postgresql-{{.project__version}}
./configure --prefix={{.project__prefix}}

make -j4
make install prefix={{.buildroot}}

cd {{.buildroot}}
find bin/ -type f | xargs strip -s

cd {{.inpack__pack_dir}}/deps
rm -rf postgresql-{{.project__version}}

%files

