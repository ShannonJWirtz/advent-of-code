# Further thoughts on part 2:

# This felt like a pen and paper puzzle to me.
# I thought a lot about the specifics of the mapping from number to segment
# This wouldn't be scalable for larger mappings
# I believe there's a performative general way to solve these types of problems.
# Probably by framing it as an exact cover problem https://en.wikipedia.org/wiki/Exact_cover
# Solved using dancing links: https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html
# But what is the set, and what is the collection of subsets?

# Could also brute force it, as there are only 7! = 5040 different mappings
# Each mapping takes an instant to check: do we have all 10 of the original number codes?
