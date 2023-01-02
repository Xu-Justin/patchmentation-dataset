# Patchmentation Dataset

This datasets are used to benchmark patch augmentation performance of [patchmentation](https://github.com/Xu-Justin/patchmentation).

## Dependency

* Using PIP

  ```bash
  pip install -r requirements.txt
  ```

* Using Docker (recommended)
  
  ```bash
  docker pull jstnxu/patchmentation:dataset
  docker run -it \
    -v {cache_folder}:/root/.cache/patchmentation-data \
    -v {data_folder}:/workspace/data \
    jstnxu/patchmentation:dataset /bin/bash
  ```
  
  * change `{cache_folder}` to local path to save cache.

  * change `{data_folder}` to local path to save generated data.

## Dataset Spesification

* **Training Dataset**

  <details> <summary> <b> <code> train-pascal-voc-2007 </code> </b> </summary>
    
    * Number of Images: 2501
    
    * Number of Classes: 20
    
    * Source: Pascal VOC 2007 - Train

    ```bash
    python3 dataset.py --version train-pascal-voc-2007 --generate
    ```
      
  </details>

  <details> <summary> <b> <code> train-pascal-voc-2007-tiny </code> </b> </summary>
    
    * Number of Images: 200
    
    * Number of Classes: 20
    
    * Source: Pascal VOC 2007 - Train

    ```bash
    python3 dataset.py --version train-pascal-voc-2007-tiny --generate --batch 2
    ```
  
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

    <br>

    ```bash
    python3 dataset.py --version train-pascal-voc-2007-v1 --generate --batch 30
    ```
  
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

    <br>

    ```bash
    python3 dataset.py --version train-pascal-voc-2007-v2 --generate --batch 30
    ```
  
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

    <br>

    ```bash
    python3 dataset.py --version train-pascal-voc-2007-v3 --generate --batch 30
    ```
  
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

    <br>

    ```bash
    python3 dataset.py --version train-pascal-voc-2007-v4 --generate --batch 30
    ```
  
  </details>

  <details> <summary> <b> <code> train-penn-fudan-ped-person </code> </b> </summary>
    
    * Number of images: 100
    
    * Number of Classes: 1
    
    * Source: Penn Fudan Ped

    ```bash
    python3 dataset.py --version train-penn-fudan-ped-person --generate --batch 100
    ```
  
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

    <br>

    ```bash
    python3 dataset.py --version train-campus --generate --batch 50
    ```
        
  </details>
  
* **Validation Dataset**
  
  <details> <summary> <b> <code> valid-pascal-voc-2007 </code> </b> </summary>
    
    * Number of Images: 2,510
    
    * Number of Classes: 20
    
    * Source: Pascal VOC 2007 - Val

    ```bash
    python3 dataset.py --version valid-pascal-voc-2007 --generate
    ```
      
  </details>

  <details> <summary> <b> <code> valid-penn-fudan-ped-person </code> </b> </summary>
    
    * Number of images: 70
    
    * Number of Classes: 1
    
    * Source: Penn Fudan Ped

    ```bash
    python3 dataset.py --version valid-penn-fudan-ped-person --generate
    ```
  
  </details>

  <details> <summary> <b> <code> valid-campus </code> </b> </summary>
    
    * Number of images: 256
    
    * Number of Classes: 1
    
    * Source: Campus - Garden1

    ```bash
    python3 dataset.py --version valid-campus --generate
    ```
  
  </details>
  
* **Test Dataset**
  
  <details> <summary> <b> <code> test-pascal-voc-2007 </code> </b> </summary>
    
    * Number of Images: 4,952
    
    * Number of Classes: 20
    
    * Source: Pascal VOC 2007 - Test

    ```bash
    python3 dataset.py --version test-pascal-voc-2007 --generate
    ```
      
  </details>

  <details> <summary> <b> <code> test-campus </code> </b> </summary>
    
    * Number of images: 11,538
    
    * Number of Classes: 1
    
    * Source: Campus - Garden1

    ```bash
    python3 dataset.py --version test-campus --generate
    ```
  
  </details>


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

---

This project was developed as part of thesis project, Computer Science, BINUS University.
