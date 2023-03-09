# Framework to analyze Delphes events for the pp -> ttbar -> bWZ bW process

Setup to analyze the process and perform plots using ROOT and RDataFrames

# Getting started - first setup to be done once

Do this only once to start the framework

```
source /cvmfs/cms.cern.ch/cmsset_default.sh # add this in your ~/.bashrc file to make it automatically when connecting on brux
cmsrel CMSSW_12_5_2
cd CMSSW_12_5_2/src
cmsenv
git clone git@github.com:mstamenk/topbWZ-analysis.git
cd topbWZ-analysis
source setup.sh
```

# To be done every time you log in into brux and want to work

```
source /cvmfs/cms.cern.ch/cmsset_default.sh # if not in ~/.bashrc file - though recommend to add it 
cd workdir/CMSSW_12_5_2/src/
cmsenv
cd topbWZ-analysis/
source setup.sh
```

Also recommend to add an `alias` in the `~/.bashrc`

```
# in ~/.basrhc
alias topbWZ-latest="cd workdir/CMSSW_12_5_2/src/; cmsenv; cd topbWZ-analysis; source setup.sh"
```

Then every time you log in into brux, just type

```
topbWZ-latest # use autocomplete normally the command will be picked up by your terminal (otherwsie source ~/.bashrc after editting)
```

# Run the framework



