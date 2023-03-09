# Script to plot Delphes samples 

import os, ROOT

ROOT.gROOT.SetBatch(ROOT.kFALSE) #(sets batch mode, set to kTRUE if you want to do many plots at once)
ROOT.ROOT.EnableImplicitMT() # enables the multi-threading to speed things up

ROOT.gSystem.Load('libDelphes')

# Open the file

path = '/isilon/data/users/mstamenk/spanet-hhh-samples/MG5_aMC_v3_4_1/GF_HHH_loop_sm_c3d4-spanet/Events/run_01_decayed_1/' # to be changed to your Delphes file

f_in = 'tag_1_delphes_events'

df = ROOT.RDataFrame('Delphes', path + '/' + f_in + '.root') # open RDataFrame called df


# plot 1 variable
var = 'Particle.PID'
nbins = 30
xmin = 0
xmax = 30

# book histogram for the variable with nbins, xmin, xmax
h = df.Histo1D((var,var,nbins,xmin,xmax),var) # This here will plot all particles per event projected on one dimension, each event has multiple particles

h = h.GetValue() # retrieve the TH1 histogram from ROOT format for histograms
h.GetXaxis().SetTitle('Particle.PID')
h.GetYaxis().SetTitle('Unweighted MC events')
h.SetTitle('') # remove title from histogram
h.SetStats(0) # remove stats on top right corner of histogram displayed by default

# Draw histogram

c = ROOT.TCanvas() # create canvas on which to draw

# Add legend to plot
legend = ROOT.TLegend(0.6,0.6,0.9,0.9) # Canvas coordinate in %, so xmin=0.6,ymin=0.6,xmax=0.9,ymax=0.9 in that order
legend.AddEntry(h,'Particle 0 in Delphes')

h.Draw('hist e') # draw histogram with error (if you want to add second histgoram, add below h2.Draw("hist e same") to draw on same canvas

c.Print('Plot_%s.pdf'%var) # Save pdf format of the plot

# See example here on how to manipulate RDataFrames: https://nbviewer.org/url/root.cern/doc/master/notebooks/df102_NanoAODDimuonAnalysis.py.nbconvert.ipynb

# For your work, you can filter the events
# top quark pdg id = 6 (-6 for anti-top)
# Z boson pdg id = 23
# W boson pdg id = 24

# I haven't tested this, so comment out if it doens work

df = df.Define('hasTop', 'Particle.PID[abs(ParticlePID) == 6]')
df = df.Define('hasZ', 'Particle.PID[abs(ParticlePID) == 6]')
df = df.Define('hasW', 'Particle.PID[abs(ParticlePID) == 6]')

df = df.Define('goodEvent', 'hasTop && hasW && hasZ')

df = df.Filter('goodEvent') # Only select events that have top, W and Z

# You can inspect the content of a Delphes root file from outside, doing root -l  and then inside the root shell, do Delphes->Print()
# Particle corresponds to the generated particles in the MC simulation (the true particle simulated, before any reconstruction)
# Using the Electron, Muon, Jet will use the reconstructed objects after some sort of detector emulation

# To calculate mass of Z boson, for example

df_2mu = df.Filter('Muon_size == 2')
df_os = df_2mu.Filter('Muon.Charge[0] != Muon.Charge[1]')
df_mass = df_os.Define('ZMass','InvariantMass(Muon.PT, Muon.Eta, Muon.Phi, Muon.Mass)')

# And so on





