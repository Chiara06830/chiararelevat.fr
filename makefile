CC=gcc 
LDFLAGS=-Wall -Wextra -pedantic -std=c99 -g -o

c: helloworld_c.x

helloworld_c.x:  
	$(CC) src/c/helloworld.c $(LDFLAGS) bin/helloworld_c.x

OCAMLC=ocamlc
OCAMLFLAGS=-o

ocaml: helloworld_ocaml.x

helloworld_ocaml.x:
	$(OCAMLC) src/ocaml/helloworld.ml $(OCAMLFLAGS) bin/helloworld_ocaml.x
	rm -f src/ocaml/*.cmi src/ocaml/*.cmo
