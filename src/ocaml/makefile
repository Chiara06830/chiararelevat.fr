OCAMLC=ocamlc
OCAMLFLAGS=-o

ocaml: helloworld_ocaml.x

helloworld_ocaml.x:
	$(OCAMLC) src/ocaml/helloworld.ml $(OCAMLFLAGS) bin/helloworld_ocaml.x
	rm -f src/ocaml/*.cmi src/ocaml/*.cmo
