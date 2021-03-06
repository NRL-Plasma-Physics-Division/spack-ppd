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

Install Molpro and keep the stage directory for tuning and testing:

```shell
$ spack install --keep-stage molpro %gcc@10.3.0 ^mpich@8.1.5
```

The package tuning and testing process will run molpro to establish some tuning parameters and 
perform some tests, requiring access to a compute node, so start an interactive job:

```shell
$ qsub -l ccm=1 -l select=1:ncpus=128:mpiprocs=128 -A NRLDC31794610 -q standard -l walltime=02:00:00 -I
```

Go to the staging directory and perform the tuning process which will
likely take 20 minutes or more.

```shell
$ spack load /hmzfood
$ spack cd --stage-dir molpro
$ cd spack-src
$ make tuning
```

Once the tuning process is complete, you will have a file named `tuning.rc` in the `spack-src/lib` folder. 
You can either copy the file to `${MOLPRO_PREFIX}/molpro_2021.1/lib/tuning.rc` or copy the contents to 
`${HOME}/.molprorc`. The former is probably the best approach since the tuning is specific to
a given build of Molpro. To determine `${MOLPRO_PREFIX}` for the given build, run the following command
and match the hash from the stage/build folder with the hash from the command's output:

```shell
spack find --paths molpro
```

Finally, you can/should run the tests provided with Molpro:

```shell
$ make MOLPRO_OPTIONS='-n2' test
```

### Molpro-Narwhal Lessons Learned

TODO: So far, Molpro only runs on one node. This is probably an issue with mpich and global arrays.
Possible remedy is to run tests in globalarrays to debug. Tried globalarrays variants 
`armci=[mpi-ts, mpi-pr]` with no luck.

Tried adding `make tuning` and `make test` steps to spack package, but molpro script looks
for nodefile and expects to be run on compute nodes.

Tried running tuning on multiple MPI processes (`make MOLPRO_OPTIONS='-n128 -m28g' tuning`),
but it seems it is meant for only one process. Or, maybe the number of processes is handled
automatically and should just do `make tuning` like the instrucions say (not
`make MOLPRO_OPTIONS='-n1 -m28g' tuning`).

Tried making the spack package as a CMakePackage, but couldn't figure out how to get the tests
to build. The resulting executable seemed to run fine on one node, and the package file is
`package_CMake_package.py`.

TODO: Latest build using cray-libsci + cray-mpich (from modules) has core dump at the end of successful job. 
Doesn't seem to happen when using mpich + openblas + netlib-lapack + netlib-scalapack, but mpich and libsci 
from modules seems more efficient.  Should try getting a stack trace to see what is happening at job termination.

See [the Molpro manual](https://www.molpro.net/manual/doku.php?id=general_program_structure#memory_allocation) 
for info on allocating memory on a given machine. For narwhal standard nodes with 256GB RAM, perhaps these values work:

- `-n 40 -m 375m -G 5000m` (40 CPUs on one node)
- `-n 30 -m 575m -G 5750m`
- `-n 20 -m 975m -G 6500m`
- `-n 2 -m 11775m -G 7850m`

Setting `ARMCI_DEFAULT_SHMMAX` in `spack load molpro` but not sure it matters.

