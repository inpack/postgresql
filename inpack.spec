[project]
name = postgresql
version = 9.6.5
vendor = postgresql.org
homepage = https://www.postgresql.org
groups = dev/db
description = The world's most advanced open source database

%build
PREFIX="{{.project__prefix}}"

cd {{.inpack__pack_dir}}/deps

if [ ! -f "postgresql-{{.project__version}}.tar.bz2" ]; then
    wget https://ftp.postgresql.org/pub/source/v{{.project__version}}/postgresql-{{.project__version}}.tar.bz2
fi
if [ ! -d "postgresql-{{.project__version}}" ]; then
    tar -vxjf postgresql-{{.project__version}}.tar.bz2
fi


mkdir -p {{.buildroot}}/{bin,data,etc,lib,share}

cd postgresql-{{.project__version}}
./configure --prefix={{.project__prefix}}

make -j4
make install prefix={{.buildroot}}

cd {{.buildroot}}
strip -s bin/clusterdb
strip -s bin/createdb
strip -s bin/createlang
strip -s bin/createuser
strip -s bin/dropdb
strip -s bin/droplang
strip -s bin/dropuser
strip -s bin/ecpg
strip -s bin/initdb
strip -s bin/pg_archivecleanup
strip -s bin/pg_basebackup
strip -s bin/pgbench
strip -s bin/pg_config
strip -s bin/pg_controldata
strip -s bin/pg_ctl
strip -s bin/pg_dump
strip -s bin/pg_dumpall
strip -s bin/pg_isready
strip -s bin/pg_receivexlog
strip -s bin/pg_recvlogical
strip -s bin/pg_resetxlog
strip -s bin/pg_restore
strip -s bin/pg_rewind
strip -s bin/pg_test_fsync
strip -s bin/pg_test_timing
strip -s bin/pg_upgrade
strip -s bin/pg_xlogdump
strip -s bin/postgres
strip -s bin/psql
strip -s bin/reindexdb
strip -s bin/vacuumdb

rm -fr /include

cd {{.inpack__pack_dir}}/deps
rm -rf postgresql-{{.project__version}}

%files
