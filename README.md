# Patchmentation Dataset

This datasets are used to benchmark patch augmentation performance of [patchmentation](https://github.com/Xu-Justin/patchmentation).

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

| Priority* |    Arguments   |        Type       | Description                                                                                                      |
|:---------:|:--------------:|:-----------------:|------------------------------------------------------------------------------------------------------------------|
|     -     |   `--version`  | one or more `str` | Dataset version(s).                                                                                              |
|     -     |  `--overwrite` |    `store_true`   | Overwrite existing dataset / zip.                                                                                |
|     -     |    `--batch`   |       `int`       | Number of batch to generate (default=`1`)                                                                        |
|     1     |  `--generate`  |    `store_true`   | Generate the dataset. If `overwrite` is true, it will remove the dataset (if exists) before generating.          |
|     2     |     `--zip`    |    `store_true`   | Zip the dataset. If `overwrite` is true, it will remove the dataset zip (if exists) before zipping.              |
|     3     |   `--upload`   |    `store_true`   | Upload the dataset zip.                                                                                          |
|     4     | `--remove-zip` |    `store_true`   | Remove the dataset zip, if exists.                                                                               |
|     5     |  `--download`  | one or more `url` | Download the dataset zip. If `overwrite` is true, it will remove the dataset zip (if exists) before downloading. |
|     6     |    `--unzip`   |    `store_true`   | Unzip the dataset zip. If `overwrite` is true, it will remove the dataset (if exists) before unzipping.          |
|     7     |  `--validate`  |    `store_true`   | Validate the dataset.                                                                                            |
|     8     |   `--remove`   |    `store_true`   | Remove the dataset, if exists.                                                                                   |

**Smaller priority number will be executed first*

## Dataset Spesification

* **Training Dataset**

  <details> <summary> <b> <code> train-pascal-voc-2007 </code> </b> </summary>
    
    * Number of Images: 2501
    
    * Number of Classes: 20
    
    * Source: Pascal VOC 2007 - Train
      
  </details>

  <details> <summary> <b> <code> train-pascal-voc-2007-tiny </code> </b> </summary>
    
    * Number of Images: 200
    
    * Number of Classes: 20
    
    * Source: Pascal VOC 2007 - Train
  
  </details>
  
  <details> <summary> <b> <code> train-pascal-voc-2007-v1 </code> </b> </summary>
    
    * Number of Images: 2,500
    
    * Number of Classes: 20
    
    * Source: Pascal VOC 2007 - Train

    * Actions

      * `filter.FilterWidth(50, Comparator.GreaterEqual)`
      
      * `filter.FilterHeight(50, Comparator.GreaterEqual)`
      
      * `transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO)`

    * Kwargs

      * `max_n_patches = 10`
  
  </details>

  <details> <summary> <b> <code> train-pascal-voc-2007-v2 </code> </b> </summary>
    
    * Number of images: 2,500
    
    * Number of Classes: 20
    
    * Source: Pascal VOC 2007 - Train

    * Actions

      * `filter.FilterWidth(50, Comparator.GreaterEqual)`
      
      * `filter.FilterHeight(50, Comparator.GreaterEqual)`
      
      * `transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO)`

      * `filter.FilterWidth(30, Comparator.GreaterEqual)`

      * `filter.FilterHeight(30, Comparator.GreaterEqual)`

      * `transform.SoftEdge(13, 20)`

    * Kwargs

      * `max_n_patches = 20`

      * `visibility_threshold = 1.0`
  
  </details>

  <details> <summary> <b> <code> train-pascal-voc-2007-v3 </code> </b> </summary>
    
    * Number of images: 2,500
    
    * Number of Classes: 20
    
    * Source: Pascal VOC 2007 - Train

    * Actions

      * `filter.FilterWidth(50, Comparator.GreaterEqual)`
      
      * `filter.FilterHeight(50, Comparator.GreaterEqual)`
      
      * `transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO)`

    * Kwargs

      * `max_n_patches = 20`

      * `visibility_threshold = 0.8`
      
      * `ratio_negative_patch = 5.0`
      
      * `iou_negative_patch = 0.2`
  
  </details>

  <details> <summary> <b> <code> train-pascal-voc-2007-v4 </code> </b> </summary>
    
    * Number of images: 2,500
    
    * Number of Classes: 20
    
    * Source: Pascal VOC 2007 - Train

    * Actions

      * `filter.FilterWidth(50, Comparator.GreaterEqual)`
      
      * `filter.FilterHeight(50, Comparator.GreaterEqual)`
      
      * `transform.RandomResize(width_range=(50, 150), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO)`

      * `filter.FilterWidth(30, Comparator.GreaterEqual)`

      * `filter.FilterHeight(30, Comparator.GreaterEqual)`

      * `transform.SoftEdge(13, 20)`

    * Kwargs

      * `max_n_patches = 20`

      * `visibility_threshold = 0.8`
      
      * `ratio_negative_patch = 5.0`
      
      * `iou_negative_patch = 0.2`
  
  </details>

  <details> <summary> <b> <code> train-penn-fudan-ped-person </code> </b> </summary>
    
    * Number of images: 100
    
    * Number of Classes: 1
    
    * Source: Penn Fudan Ped
  
  </details>

  <details> <summary> <b> <code> train-campus </code> </b> </summary>
    
    * Number of images: 250
    
    * Number of Classes: 1
    
    * Source: Campus - Garden1, Penn Fudan Ped

    * Actions

      * `filter.FilterWidth(20, Comparator.GreaterEqual)`
      
      * `filter.FilterHeight(20, Comparator.GreaterEqual)`
      
      * `transform.RandomResize(height_range=(150, 600), aspect_ratio=transform.Resize.AUTO_ASPECT_RATIO)`

      * `transform.SoftEdge(5, 10)`

    * Kwargs

      * `max_n_patches = 30`

      * `visibility_threshold = 0.8`
        
  </details>
  
* **Validation Dataset**
  
  <details> <summary> <b> <code> valid-pascal-voc-2007 </code> </b> </summary>
    
    * Number of Images: 2510
    
    * Number of Classes: 20
    
    * Source: Pascal VOC 2007 - Val
      
  </details>

  <details> <summary> <b> <code> valid-penn-fudan-ped-person </code> </b> </summary>
    
    * Number of images: 70
    
    * Number of Classes: 1
    
    * Source: Penn Fudan Ped
  
  </details>

  <details> <summary> <b> <code> valid-campus </code> </b> </summary>
    
    * Number of images: 256
    
    * Number of Classes: 1
    
    * Source: Campus - Garden1
  
  </details>
  
* **Test Dataset**
  
  <details> <summary> <b> <code> test-pascal-voc-2007 </code> </b> </summary>
    
    * Number of Images: 4952
    
    * Number of Classes: 20
    
    * Source: Pascal VOC 2007 - Test
      
  </details>

  <details> <summary> <b> <code> test-campus </code> </b> </summary>
    
    * Number of images: ? (will be updated soon)
    
    * Number of Classes: 1
    
    * Source: Campus - Garden1
  
  </details>

---

This project was developed as part of thesis project, Computer Science, BINUS University.
