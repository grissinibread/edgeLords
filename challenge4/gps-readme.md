# I Know a Shortcut!

You're a First year student with an unfortunate schedule. Somehow you got a class in every building on campus: **Science Hall 1, Academic Hall, Markstein Hall, University Hall, Social and Behavioral Science Building, Kellogg Library, Science Hall 2, and Extended Learning Building**. Not only are they all over the place, they're also all on the top floors of each building. Being a first year, you're not crushed by this fact and decide this is the perfect opportunity to find the most perfect route between all the buildings.

## Your Task

Find the **shortest** path between each building that allows you to make it to your classes on time and then back to your starting building within the following constraints:

1. No moving through bushes, barriers, or walls; all nodes must be on walkable paths.

2. all distances have x, y, and z components.

3. Any building can be the starting/ending location, buildings can only be visited once except the starting/ending location. This rule does not apply to builds not listed above

4. Speed and time are negligible, the only variable is distance.

5. Curved distances or stairs can be thought as flat slopes.

6. if some paths are condition dependent, account for the **Expected Value** of the path ie `distance = path_condition * E(x)`. 

## Formatting and Outputs


## Additional map

We would like a marked up map of the path taken between each building be included in your submission, see `map.png` for a reference. Use `Empty.png` for the mark up of your path.