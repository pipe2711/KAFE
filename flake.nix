{
  description = "Flake para el desarollo de KAFE";

  inputs.nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";

  outputs =
    { self, nixpkgs }:
    let
      supportedSystems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      forEachSupportedSystem =
        f:
        nixpkgs.lib.genAttrs supportedSystems (
          system:
          f {
            pkgs = import nixpkgs { inherit system; };
          }
        );
    in
    {
      devShells = forEachSupportedSystem (
        { pkgs }:
        {
          default = pkgs.mkShell {
            packages = with pkgs; [
              antlr
              flex
              openjdk
              git
              (python3.withPackages (
                p: with p; [
                  pytest
                  antlr4-python3-runtime
                ]
              ))
              bison
            ];
          };
        }
      );
    };
}
