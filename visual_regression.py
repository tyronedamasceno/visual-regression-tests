import os
import sys
import uuid

from PIL import Image, ImageDraw

class VisualRegression:

    def __init__(self, baseline=None, test=None):
        self.baseline = baseline
        self.test = test

    def analyze(self):
        baseline = Image.open(self.baseline)
        test = Image.open(self.test)
        columns = 60
        rows = 80
        if baseline.size != test.size:
            raise RuntimeError('The screenshots must have the same size')

        baseline_vec = baseline.getdata()
        test_vec = test.getdata()

        screen_width, screen_height = baseline.size

        block_width = ((screen_width - 1) // columns) + 1
        block_height = ((screen_height - 1) // rows) + 1
        
        has_regression = False
        for y in range(0, screen_height, block_height+1):
            for x in range(0, screen_width, block_width+1):
                region_baseline= self.process_region(baseline_vec, x, y, block_width, block_height, screen_width)
                region_test = self.process_region(test_vec, x, y, block_width, block_height, screen_width)

                if region_baseline and region_test and region_baseline != region_test:
                    has_regression = True
                    draw = ImageDraw.Draw(test)
                    draw.rectangle((x, y, x+block_width, y+block_height), outline = "red")
        
        print('Successful test!')
        result_path = ''
        if has_regression:
            filename = f'result_{uuid.uuid4().hex}.png'
            test.save(filename)
            # result_path = os.path.join(os.getcwd(), filename)
            result_path = filename
            print('Visual regressions were found')
            print(f'Check result at {result_path}')
        else:
            print('Visual regressions were not found')

        return has_regression, result_path 

    def process_region(self, image_vec, x, y, width, height, scr_width):
        region_total = 0

        # This can be used as the sensitivity factor, the larger it is the less sensitive the comparison
        factor = 100

        for coordinateY in range(y, y+height):
            for coordinateX in range(x, x+width):
                try:
                    pixel = image_vec[coordinateY*scr_width + coordinateX]
                    region_total += sum(pixel)/4
                except:
                    return

        return region_total/factor


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        raise RuntimeError('You must give the 2 screenshots path')
    else:
        reg_test = VisualRegression(*args[1:])
        reg_test.analyze()

