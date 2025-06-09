{ pkgs }: {
  deps = [
    pkgs.python310
    pkgs.python310Packages.pip
    pkgs.python310Packages.setuptools
    pkgs.poetry
    pkgs.cacert
    pkgs.openssl
    pkgs.git
  ];
}
