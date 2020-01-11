# word-embedding

Create word-embedding model using skip-gram and negative sampling. This model is trained with wikipedia and opensubtitle corpus with total word = 208.807M and output feature dimension = 128.


### Requirements to use this program
--------
  - Python 2 or 3
  - Gensim
  - sklearn



### To visualizing word vector using T-SNE, run :

``` bash
$ python tsne_plot.py list_word
```
This will generate a ~332 word with list_word as a generating keyword, and create
a 2D plot of word vector.

### Example :
```bash
$ python plot-tsne.py siang komputer sendu kaki mati apel relativitas emansipasi jokowi

```

### Plot example :
![alt text](tsne_plot.jpg)
### Corpus source :
Wikipedia : [https://dumps.wikimedia.org/idwiki/20200101/](https://dumps.wikimedia.org/idwiki/20200101/)\
opensubtitle : [http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2018/mono/OpenSubtitles.raw.id.gz](http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2018/mono/OpenSubtitles.raw.id.gz)
