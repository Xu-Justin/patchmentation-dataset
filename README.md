# patchmentation-benchmarking

Dataset spesifications used to benchmark patch augmentation performance of [patchmentation](https://github.com/Xu-Justin/patchmentation).

## Quickstart

* Run the following commands to install the requirements.

```bash
pip install -r requirements.txt
```

* Run the following commands to generate the dataset.

```bash
python3 dataset.py --version [version] --generate
```

## Arguments



## Dataset Spesification

* **Training Dataset**

  <details> <summary> <b> <code> train-pascal-voc-2007-tiny </code> </b> </summary>
    
    * Number of Images: 1,000
    
    * Source: Pascal VOC 2007 - Train
  
  </details>
  
  <details> <summary> <b> <code> train-pascal-voc-2007-v1 </code> </b> </summary>
    
    * Number of Images: 50,000
    
    * Source: Pascal VOC 2007 - Train

    * Actions

      * `filter.FilterWidth(50, Comparator.GreaterEqual)`
      
      * `filter.FilterHeight(50, Comparator.GreaterEqual)`
      
      * `transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO)`

    * Kwargs

      * `max_n_patches = 10`
  
  </details>

  <details> <summary> <b> <code> train-pascal-voc-2007-v2 </code> </b> </summary>
    
    * Number of images: 50,000
    
    * Source: Pascal VOC 2007 - Train

    * Actions

      * `filter.FilterWidth(50, Comparator.GreaterEqual)`
      
      * `filter.FilterHeight(50, Comparator.GreaterEqual)`
      
      * `transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO)`

      * `filter.FilterWidth(30, Comparator.GreaterEqual)`

      * `filter.FilterHeight(30, Comparator.GreaterEqual)`

      * `transform.SoftEdge(13, 20)`

    * Kwargs

      * `max_n_patches = 10`
  
  </details>

    <details> <summary> <b> <code> train-pascal-voc-2007-v3 </code> </b> </summary>
    
    * Number of images: 50,000
    
    * Source: Pascal VOC 2007 - Train
    
    * Validation: `valid-pascal-voc-2007`

    * Actions

      * `filter.FilterWidth(50, Comparator.GreaterEqual)`
      
      * `filter.FilterHeight(50, Comparator.GreaterEqual)`
      
      * `transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO)`

    * Kwargs

      * `max_n_patches = 20`

      * `visibility_threshold = 1.0`
  
  </details>
  
* **Validation Dataset**
  
  <details> <summary> <b> <code> valid-pascal-voc-2007 </code> </b> </summary>
    
    * Number of Images: 2510
    
    * Source: Pascal VOC 2007 - Val
      
  </details>
  
* **Test Dataset**
  
  <details> <summary> <b> <code> test-pascal-voc-2007 </code> </b> </summary>
    
    * Number of Images: 4952
    
    * Source: Pascal VOC 2007 - Test
      
  </details>
