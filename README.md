# loci
Land Opportunity & Characterization Insights model.

## Installation
1. Clone the repo
    ```commandline
    git clone git@github.com:NREL/loci.git
    ```

2. Move into the local repo
    ```command line
    cd loci
    ```

3. Recommended: Setup virtual environment with `conda`/`mamba`:
    ```commandline
    mamba env create -f environment.yml
    mamba activate loci
    ```
    Note: You may choose an alternative virtual environment solution; however, installation of dependencies is not guaranteed to work.

4. Install `loci`:
    - For users: `pip install .`
    - For developers: `pip install -e '.[dev]'`

5. **Developers Only** Install pre-commit
```commandline
pre-commit install
```

## Usage
Refer to the [Usage](USAGE.md) documentation.
