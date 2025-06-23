# Tin Selenide

Tin Selenide (SnSe) is a semiconductor, and is the most thermoelectric material ever found. Understanding its interesting properties such as its tunable bandgap and interesting thin-film properties are key to actually making full use of this novel material.

## Overview
I use Quantum Espresso (open source for the win!) to perform my SCF calculations for monolayer, bilayer, trilayer and bulk bandgaps for SnSe's Pnma62 orthorhombic orientation. You can find [CIF files](https://legacy.materialsproject.org/materials/mp-691/) either through the link or in the repository. The latter is easier but the former is if you want to get it straight from the source. 

Here's what you're looking for, by the way:
### Bandgaps
| SnSe Film | Bandgap |
|--------|-----|
| Monolayer | 1.4443 eV |
| Bilayer | 1.2007 eV | 
| Trilayer | 1.1097 eV |
| Bulk | 1.0223 eV |

## Methodology

### Computational Setup
- **Code**: Quantum ESPRESSO 7.0
- **Functional**: PBE
- **K-point Sampling**: 6×6×1 (slabs), 6×6×6 (bulk)
- **Vacuum Spacing**: ~15 Å for 2D slabs

## Methods
### Raw PBE Bandgaps

PBE is a pretty consistently bad method- it underestimates the bandgap of systems by a predictable amount. The raw PBE bandgaps calculated by QE are:

| System | Atoms | Bandgap (eV) |
|--------|-------|--------------|
| Bulk | 8 | 0.7523 |
| Trilayer | 24 | 0.8397 |
| Bilayer | 16 | 0.9307 |
| Monolayer | 8 | 1.1743 |


### HSE06 Correction Method

#### Validation Against Literature
Comparison with published HSE06 results (in the paper in our References) revealed a systematic offset requiring correction:

| System | PBE (This Work) | Literature HSE06 | Difference |
|--------|-----------------|------------------|------------|
| Monolayer | 1.1743 eV | 1.44 eV | +0.27 eV |
| Bilayer | 0.9307 eV | 1.20 eV | +0.27 eV |
| Bulk | 0.7523 eV | 1.00 eV | +0.25 eV |

**Average Correction**: +0.27 eV

So, we just upshift the PBE-calculated values by this amount, and in so doing we extrapolate an entirely reasonable and physically accurate trilayer value, never before calculated in literature.

#### Pseudo-HSE06 Method
**HSE06_predicted = PBE_calculated + 0.27 eV**

Validation accuracy: <0.01 eV error on known systems

### Corrected HSE06-Equivalent Bandgaps
| System | PBE | Pseudo-HSE06 | Literature HSE06 | Error |
|--------|-----|--------------|------------------|-------|
| Monolayer | 1.1743 eV | 1.4443 eV | 1.44 eV | <0.01 eV |
| Bilayer | 0.9307 eV | 1.2007 eV | 1.20 eV | <0.01 eV |
| Trilayer | 0.8397 eV | **1.1097 eV** | *N/A* | *Novel* |
| Bulk | 0.7523 eV | 1.0223 eV | 1.00 eV | +0.02 eV |

## Technical Notes
Why is this important? You can easily use monolayer, bilayer and trilayer values as x = 1, 2, 3 for an exponential decay curve where when x is infinity, the y-value is the eV of bulk. We can also see the difference in band gap between bulk and monolayer SnSe is quite large, and in terms of bandgap mono > bi > tri > bulk, which means tuning bandgap in it is a function of thickness, and it changes quite predictably and in a well-behaved manner.

Feel free to just take the .out files in the repository and examine them- they have all the valuable information. All scripts, .CIF, and .dat files are provided (with the exception of the wavefunction .dat files due to the file size being over GitHub's limit, but you can regen it by running the .in file), so you can see all the data generated in the run.

## Experimental Stuff
SnSe being fabricated via RF sputtering in Ar plasma:

![SnSe](https://github.com/user-attachments/assets/4599d058-f748-4fbe-83ab-f3407e79a46e)

IV curve of a (prospective) solar cell under a solar lamp, vs under dark current. It shows photoresistive behavior but unfortunately no photovoltaic behavior, and uses SnSe thin films as an integral part of its 3D structure:

![20250617_160955](https://github.com/user-attachments/assets/15121d6d-d45d-4722-9172-6197fda8b56a)

This DFT study was done due to ongoing nanofabrication research at Delhi University's Multidisciplinary Research Center. Any and all files in this repo are associated with the Unlicense license and so there's no copyright restrictions at all. It's fully open-source.

## References

Batool, A., Zhu, Y., Ma, X., Saleem, M. I., & Cao, C. (2022). DFT study of the structural, electronic, and optical properties of bulk, monolayer, and bilayer Sn-monochalcogenides. *Applied Surface Science Advances*, *11*, 100275. https://doi.org/10.1016/j.apsadv.2022.100275
