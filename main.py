import sys
import os.path
from typing import Literal


def main() -> None:
    args = sys.argv[1:]
    try:
        fps, in_dir, out_file = validate_args(args)
    except:
        print("Usage: python main.py [24|30|60] [img_dir] [out_file]")
        return
        
    # TODO: open all images
    # TODO: get time from image metadata
    # TODO: calculate number of frames each image should last for
    # TODO: stitch images into video
    # TODO: write video


def validate_args(args: list[str]) -> tuple[Literal[24, 30, 60], str, str]:
    assert len(args) == 3
    fps, in_dir, out_file = args
    assert fps in ["24", "30", "60"]
    assert os.path.exists(in_dir)
    # TODO: ensure that in_dir is a path to a directory that is filled with images
    assert not os.path.exists(out_file) # we don't want to overwrite an existing file
    return int(fps), in_dir, out_file
    

if __name__ == "__main__":
    main()