# word-embedding

Create word-embedding model using skip-gram. This model trained with wikipedia and opensubs corpus with total word = 208.807M and output feature dimension = 128.


### Requirements to use this program
--------
  - Python 2 or 3
  - Gensim
  - sklearn



### To visualizing word vector using T-SNE, run :

``` bash
$ python3 tsne_plot.py list_word
```
This will generate a ~332 word with list_word as a generating keyword, and create
a 2D plot of word vector.

### Example :
```bash
$ python plot-tsne.py siang musik komputer mati bakteri senja rindu
```

Example of plot can be seen on tsne_plot.jpg file

### Source :
[Wikipedia](https://dumps.wikimedia.org/idwiki/20200101/)
[opensubs](http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2018/mono/OpenSubtitles.raw.id.gz)