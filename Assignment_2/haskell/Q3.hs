import System.IO  
import Control.Monad

main::IO()
main = do
    matM <- readMatFile "data_file_for_Q3/Mat-M.txt" 
    --matN <- readMatFile "data_fiel_for_Q3/Mat-M.txt"
    print matM
   -- print matN
-- hello test function 
readMatFile :: String -> IO  [[Double]]
readMatFile fileName = do  
        handle <- openFile fileName ReadMode
        contents <- hGetContents handle
        let singleLine = lines contents
            list = map (f.words) singleLine
        hClose handle  
        return list 
        where 
            f :: [String] -> [Double]
            f = map read 


matProduct :: [[Double]]->[[Double]]->[[Double]]
matProduct matA matB = [[ sum $ map ( \(x,y)-> x*y) $  zip x y  | y <- matB] | x<-matA]


matTranspose :: [[Double]]->[[Double]]
matTranspose [] = []
matTranspose matA = if f1 matA == []then [] else f1 matA : (matTranspose . f2) matA
    where
        f1 x = [a|(a:as)<-x]
        f2 x = [as|(a:as)<-x]

