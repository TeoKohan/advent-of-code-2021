import System.IO

main = do  
    file <- readFile "input"
    let ls = lines file
    let ns = map (\x -> (read x :: Int)) ls
    let a = show . descending $ ns
    let b = show . descending . windows $ ns
    writeFile "output" (unlines[a,b])

windows :: [Int] -> [Int]
windows (x:xs)
    | length xs < 2 = []
    | otherwise = (x + xs !! 0 + xs !! 1) : windows xs

descending :: [Int] -> Int
descending []     = 0
descending [x]    = 0
descending (x:xs) = (if head xs > x then 1 else 0) + descending xs