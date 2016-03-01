# sfm-weibo-harvester master docker container

A docker container for running sfm-weibo-analysis demo.
The UI code must be mounted as `/opt/sfm-weibo-datasts`, the sfm-weibo-haverster code as `/opt/sfm-weibo-harvester`, the sfm-utils code as `/opt/sfm-utils` and the warcprox code as `/opt/warcprox`.
For example:

```python
volumes:
    - "/my_directory/sfm-weibo-weibonalysis:/opt/sfm-weibo-datasts"
    - "/my_directory/sfm-weibo-harvester:/opt/sfm-weibo-harvester"
    - "/my_directory/sfm-utils:/opt/sfm-utils"
    - "/my_directory/warcprox:/opt/warcprox"
```

