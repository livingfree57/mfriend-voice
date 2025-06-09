{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.setuptools
    pkgs.poetry
    pkgs.cacert
    pkgs.openssl
    pkgs.git
    pkgs.lsof
  ];
}
