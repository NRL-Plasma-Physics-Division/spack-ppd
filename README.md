# spack-ppd
This is the NRL Plasma Physics Division spack package repo.

## Installation

Clone this repo somewhere (like $HOME/opt). Copy the `.spack/repos.yaml` 
file to `$HOME/.spack/repos.yaml`, and update it to point to `spack-ppd`:

```yaml
repos:
  - $HOME/opt/spack-ppd # or wherever you put it
  - $spack/var/spack/repos/builtin
```

## Building Molpro on Narwhal

Molpro is a commercial code, so you will need to obtain the tarball and update
the Molpro package in `spack-ppd` to point to it. Do `spack edit molpro` and
update the `url` line to point to the file.

We want to use a specific mpich module on the system and build a particular variant of
Global Arrays (`armci=openib` and `scalapack=True`), 
which is all taken care of in the `.spack/packages.yaml` file. 
The lines you need to add to `.spack/packages.yaml` are in `.spack/packages-narwhal.yaml`
in this repo.
Be sure not to change any of the other contents of the file, and only copy in the `mpich`
and `globalarrays` blocks (you only want one top-level `packages:` entry).

Build and install Molpro with the command `spack install molpro %gcc@10.3.0 ^mpich@8.1.5`.
