from time import sleep

from tqdm import tqdm

with tqdm(total=100, ncols=80, colour='green', desc='Buscando Tweets') as pbar:
    for i in range(10):
        sleep(0.1)
        pbar.update(10)
