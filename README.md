# word-embedding

Create word-embedding model using skip-gram and negative sampling. This model is trained with wikipedia and opensubtitle corpus with total word = 269.246M and output feature dimension = 256.


### Requirements to use this program
--------
  - Python 2 or 3
  - Gensim
  - sklearn

### Model : [w2v_embedding_269M_256dim](https://drive.google.com/open?id=1Pl4dlrupwIGjRhI_wyLBvm6WZqYEHOlv)

### To visualizing word vector using T-SNE, run :
---------
``` bash
$ python tsne_plot.py list_word
```
This will generate a ~500 word with list_word as a generating keyword, and create
a 2D plot of word vector.

### Example :
--------
```bash
$ python plot-tsne.py siang komputer sendu kaki mati apel relativitas emansipasi jokowi

```

### Plot example :
--------
![alt text](tsne_plot.jpg)

### Corpus source :
Wikipedia (~5.6GB) : [https://dumps.wikimedia.org/idwiki/20200101/](https://dumps.wikimedia.org/idwiki/20200101/)\
opensubtitle (~702MB) : [http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2018/mono/OpenSubtitles.raw.id.gz](http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2018/mono/OpenSubtitles.raw.id.gz)
