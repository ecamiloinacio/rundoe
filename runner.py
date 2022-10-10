import random
import subprocess
from sys import stderr, stdout
from itertools import product

class Runner:
    # TODO: validate config input
    def __init__(self, config):
        self.__config = config
        self.__factors = {}
        self.__args_ref = {}
        for factor in config['factors']:
            self.__factors[factor['name']] = factor['values']
            self.__args_ref[factor['name']] = factor['arg']
        
        self.__trials = list(dict(zip(self.__factors.keys(), values)) \
                        for values in product(*self.__factors.values()))

    def __build_cmd(self, trial):
        cmd = [self.__config['cmd']]
        for arg_key, arg_val in trial.items():
            cmd.append(self.__args_ref[arg_key])
            cmd.append(str(arg_val))
        return cmd

    def run(self):
        for exp_repl in range(1, self.__config['exp_repls']+1):
            if not self.__config['quiet']:
                print(f'Experiment replication #{exp_repl}')    
            trials = self.__trials.copy()
            random.shuffle(trials)
            for trial in trials:
                for trial_rept in range(1, self.__config['trial_repts']+1):
                    if not self.__config['quiet']:
                        print(f'Trial repetition #{trial_rept}')
                    self.__run_trial(trial)
    
    def __run_trial(self, trial):
        cmd = self.__build_cmd(trial)
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        if not self.__config['quiet']:
            print(stdout.decode('utf-8'))