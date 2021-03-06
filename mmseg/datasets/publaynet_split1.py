from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class publaynet_split1Dataset(CustomDataset):
    """table_structure1
    """
    # CLASSES = ('title', 'text', 'figure', 'table', 'list')
    # PALETTE = [[50, 255, 0],[255, 0, 0],[0, 255, 255],[255, 192, 203],[100, 0, 255]]

    CLASSES = ('background','text', 'table', 'figure')
    PALETTE = [[120, 120, 120],[255, 0, 0],[0, 255, 0],[0, 0, 255]]
    def __init__(self, **kwargs):
        super(publaynet_split1Dataset, self).__init__(
            img_suffix='.jpg',
            seg_map_suffix='.png',
            reduce_zero_label=False,
            **kwargs)