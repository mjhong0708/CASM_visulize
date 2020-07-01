# CASM_visulize

[CE_dataquery.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d8b3a10-f126-4e9a-84d3-b68ae9c300a5/CE_dataquery.py)

- Required files : `eci.json` for ECI and `fit_blahblah.json` for fitting info.
- Run by command `CE_dataquery` by adding this file to `PATH`
- Or run this command `python3 CE_dataquery.py` with copying file into your working directory.
- At first run, you see:

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bfa00922-bebd-4b68-904b-d044dfba822a/Untitled.png]

- When done, correlation matrix is written in `corr.json` and energy hull by DFT is written in `energyHull_calculated.json`.
- Finally, full energy hull data is written into `energyHull.csv`.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/42a68936-1aae-434f-a0a2-64c48c527e82/Untitled.png]


## 2.Plot Energy Convex Hull

[CE_plotEnergyHull.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a360120e-9e21-4137-a7c0-f802f7547f60/CE_plotEnergyHull.py)

- Required file : only `energyHull.csv`
- Run by `python2 CE_plotEnergyHull.py`.
- Sample of energy convex hull plot

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/201a2d7b-42ad-4e48-9c97-38531d681100/energyHull.png]

