{ pkgs }: {
    deps = [
      pkgs.python3 ./get-pip.py
      pkgs.python3 ./get-pip.py
      pkgs.cowsay
    ];
}