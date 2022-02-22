import PyDSTool as de
import matplotlib.pyplot as plt

# control this with the following
t_kitchen = 20.0;         # kitchen (ambient temperature)
t_thermostat = 4.0;       # thermostat nominal setting
thermo_range = 0.5;       # switching distance
fridge_cap = 50000;       # thermal capacity, Joule/deg
freeze_cap = 50000;       # thermal capacity, Joule/deg

# events for thermostat. Motor on when above 4.5 deg
on_event_args = {'name': 'motor_on', 'term': True}
switch_on_ev = de.makeZeroCrossEvent(
    't1-t_on', 1, on_event_args, varnames =['t1'], parnames=['t_on']) 

# Motor off when below 3.5 deg
off_event_args = {'name': 'motor_off',
                  'eventtol': 10,
                  'eventdelay': 0,
                  'starttime': 0,
                  'active': True,
                  'term': True,
                  'precise': True}
switch_off_ev = de.makeZeroCrossEvent(
    't1-t_off', -1, off_event_args, varnames =['t1'], parnames=['t_off']) 

# initial state of the fridge, kitchen temperature
icdict = { 't1': t_kitchen, 't2' : t_kitchen }

# parameter dictionary, re-used for the two models
pardict = dict(Ck1 = fridge_cap, Ck2 = freeze_cap, R1 = 10, R2 = 4, 
               P1 = 400, P2 = 400, tenv = t_kitchen, 
               t_on=t_thermostat+thermo_range, 
               t_off=t_thermostat-thermo_range)

# differential equation for fridge with motor on
# since the fridge is a fairly slow system, the step size can be
# larger, 10 s in this case
fridge_on_args = {
    'pars' : pardict,
    'xdomain' : { 't1': [t_thermostat - thermo_range, 100] },
    'varspecs' : { 't1': '1/Ck1*(R1*(tenv - t1) - P1)',
                   't2': '1/Ck2*(R2*(tenv - t2) - P2)', }, 
    'events' : switch_off_ev, 
    'name' : 'fridge_on',
    'algparams' : { 'init_step' : 10 }}

# differential equation for fridge with motor off
fridge_off_args = {
    'pars' : pardict,
    'xdomain' : { 't1': [ -100, t_thermostat + thermo_range] },
    'varspecs' : { 't1': '1/Ck1*(R1*(tenv - t1))',
                   't2': '1/Ck2*(R2*(tenv - t2))', }, 
    'events' : switch_on_ev, 
    'name' : 'fridge_off',
    'algparams' : { 'init_step' : 10 }}
                   
# The generators are the differential equation solvers
# the 'embed' creates a re-usable model for these
all_model_names = ['fridge_working', 'fridge_off']
fridge_working = de.embed(
    de.Generator.Vode_ODEsystem(fridge_on_args), name=all_model_names[0])
fridge_off = de.embed(
    de.Generator.Vode_ODEsystem(fridge_off_args), name=all_model_names[1])

# from that create the internal model interfaces
fridge_working_mi = de.intModelInterface(fridge_working)
fridge_off_mi = de.intModelInterface(fridge_off)

# next step, model info entries
# these combine the different models with events, and the transition to
# the other model when the event is triggered
fridge_working_info = de.makeModelInfoEntry(
    fridge_working_mi, all_model_names, 
    [ ('motor_off', ('fridge_off', 
                     de.EvMapping(model=fridge_off_mi.model))) ])
fridge_off_info =  de.makeModelInfoEntry(
    fridge_off_mi, all_model_names, 
    [ ('motor_on', ('fridge_working', 
                    de.EvMapping(model=fridge_working_mi.model))) ])

# combine these together
modelInfoDict = de.makeModelInfo([fridge_working_info, fridge_off_info])

# make the hybrid model
totalfridge = de.Model.HybridModel(dict(name='fridge', modelInfo=modelInfoDict))

# calculate the response, 4 hours
totalfridge.compute(trajname='4hours', tdata=[0, 24*3600], ics=icdict)

# and plot
plotData = totalfridge.sample('4hours', dt = 60)

plt.ylabel('t1, t2 [C]')
plt.xlabel('time [s]')
friline = plt.plot(plotData['t'], plotData['t1'])
freline = plt.plot(plotData['t'], plotData['t2'])

plt.show()
