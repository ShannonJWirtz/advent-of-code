def depth_sum(nums):
    return sum(n2 > n1 for n1, n2 in zip(nums[:-1], nums[1:]))

def get_windowed_nums(nums):
    return [sum(nums[n:(n+3)]) for n in range(len(nums) - 2)]

def windowed_depth_sum(nums):
    return depth_sum(get_windowed_nums(nums))

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    nums = [int(l.strip()) for l in lines]
    print('problem 1 answer: ', depth_sum(nums))
    print('problem 2 answer: ', windowed_depth_sum(nums))
