import System.IO

main = do  
    file <- readFile "input"
    let ls = lines file
    let ws = map words ls
    let ts = map (\x -> (x !! 0, x !! 1)) ws
    let ns = map (\(x, y) -> (x, read y :: Int)) ts
    let is = reverse ns
    let linear = linear_submarine is
    let rotation = rotation_submarine is
    print linear
    print rotation

add_tuple :: (Num a) => (a, a) -> (a, a) -> (a, a)
add_tuple (a, b) (c, d) = (a+c, b+d)

linear_submarine :: [(String, Int)] -> (Int, Int)
linear_submarine []                  = (0, 0)
linear_submarine (("forward", x):xs) = (x,  0) `add_tuple` linear_submarine xs
linear_submarine (("up",      x):xs) = (0, -x) `add_tuple` linear_submarine xs
linear_submarine (("down",    x):xs) = (0,  x) `add_tuple` linear_submarine xs

aim :: [(String, Int)] -> Int
aim []               =  0
aim (("up",   x):xs) = -x + aim xs
aim (("down", x):xs) =  x + aim xs
aim (_:xs)           =  aim xs

rotation_submarine :: [(String, Int)] -> (Int, Int)
rotation_submarine []                  = (0, 0)
rotation_submarine (("forward", x):xs) = (x, x * (aim xs)) `add_tuple` rotation_submarine xs
rotation_submarine (_:xs)              = rotation_submarine xs