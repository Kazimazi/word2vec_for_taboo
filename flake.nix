{
  description = "template for python dev envs";

  # Provides abstraction to boiler-code when specifying multi-platform outputs.
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (
        system:
        let
          pkgs = import nixpkgs {
            system = "x86_64-linux";
            config.allowUnfree = true;
          };
        in
        {
          devShell = pkgs.mkShell {
            buildInputs = [
              (
                pkgs.python3.withPackages (ps: with ps; [
                  gensim
                ])
              )
            ];
          };
        }
      );
}
