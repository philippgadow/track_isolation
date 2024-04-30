import ftag
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read h5 file and plot the data
from ftag.hdf5 import H5Reader
fname = 'maya.h5'
obj = 'muons'
columns = ['pt', 'eta', 'phi', 'iffClass']
reader = H5Reader(fname, jets_name=obj, batch_size=1_000)
data = reader.load({obj: columns}, num_jets=100_000)[obj]
df = pd.DataFrame(data, columns=columns)

# select muons based on iffClass (4 for prompt, !=4 for nonprompt)
obj_prompt = df[df['iffClass'] == 4]
obj_nonprompt = df[df['iffClass'] != 4]

# plot pt for prompt and nonprompt muons
fig, ax = plt.subplots()
ax.hist(obj_prompt['pt'], bins=100, alpha=0.5, label='prompt')
ax.hist(obj_nonprompt['pt'], bins=100, alpha=0.5, label='nonprompt')
plt.xlabel('pt')
plt.ylabel('Frequency')
ax.legend(loc='upper right')
fig.savefig('pt.png')
