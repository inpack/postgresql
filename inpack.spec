[project]
name = postgresql-inner
version = 0.9.2
vendor = sysinner.com
homepage = https://www.sysinner.com
groups = dev/db
description = configuration management tool for PostgreSQL

%build
PREFIX="{{.project__prefix}}"

mkdir -p {{.buildroot}}/{bin,log}

go build -ldflags "-w -s" -o {{.buildroot}}/bin/pg_inner inner.go

%files
misc/
README.md
LICENSE


