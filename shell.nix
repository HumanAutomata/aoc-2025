let
  pkgs = import <nixpkgs> {};
in
  pkgs.mkShell {
    packages = [
      (pkgs.python3.withPackages (ps: [
        ps.numpy
      ]))
    ];

    shellHook = ''fish'';
  }
