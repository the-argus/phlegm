{
  # inputs.nixpks.url = "github:nixos/nixpkgs?ref=nixos-22.05";
  inputs.nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";

  outputs =
    { self
    , nixpkgs
    }@inputs:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };

      pythonPackages = with pkgs.python310Packages; [
        tkinter
        pyls-flake8 flake8
      ];
    in
    rec {
      devShell.${system} = pkgs.mkShell {

        nativeBuildInputs = with pkgs; [
          python310
        ] ++ pythonPackages;

        shellHook = ''
          if [ -e .venv ]; then
              source .venv/bin/activate
          fi
          echo "Entering python arcade shell..."
        '';
      };
    };
}
