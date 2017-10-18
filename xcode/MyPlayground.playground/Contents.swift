
import UIKit

extension MutableCollection {
    /// Shuffles the contents of this collection.
    mutating func shuffle() {
        let c = count
        guard c > 1 else { return }
        
        for (firstUnshuffled, unshuffledCount) in zip(indices, stride(from: c, to: 1, by: -1)) {
            let d: IndexDistance = numericCast(arc4random_uniform(numericCast(unshuffledCount)))
            let i = index(firstUnshuffled, offsetBy: d)
            swapAt(firstUnshuffled, i)
        }
    }
}

extension Sequence {
    /// Returns an array with the contents of this sequence, shuffled.
    func shuffled() -> [Element] {
        var result = Array(self)
        result.shuffle()
        return result
    }
}

var shuffleBalls = [1,2,3,4,5,6,7,8,9,10]
let oddWeights = [-1,1]
var shuffleBallWeights = [0,0,0,0,0,0,0,0,0,0]

shuffleBalls = shuffleBalls.shuffled()

print("Generating random odd ball")
var chosenBall:Int = shuffleBalls[Int(arc4random_uniform(10))]
var chosenWeight:Int = oddWeights[Int(arc4random_uniform(2))]

if let chosenBallLocation:Int = shuffleBalls.index(of: chosenBall){
    shuffleBallWeights[chosenBallLocation] = chosenWeight
}

print("ball \(chosenBall)")
print("Weight \(chosenWeight)")

print(shuffleBalls)
print(shuffleBallWeights)

print("Weighing scales: ")

print("\(shuffleBalls[0]), \(shuffleBalls[1]), \(shuffleBalls[2]) <-> \(shuffleBalls[3]), \(shuffleBalls[4]), \(shuffleBalls[5])")

var side1 = shuffleBallWeights[0] + shuffleBallWeights[1] + shuffleBallWeights[2]
var side2 = shuffleBallWeights[3] + shuffleBallWeights[4] + shuffleBallWeights[5]

if side2 > side1 {
    print("Right side heavier")
    print("\(shuffleBalls[6]), \(shuffleBalls[7]), \(shuffleBalls[8]) <-> \(shuffleBalls[3]), \(shuffleBalls[4]), \(shuffleBalls[5])")
    side1 = shuffleBallWeights[6] + shuffleBallWeights[7] + shuffleBallWeights[8]
    side2 = shuffleBallWeights[3] + shuffleBallWeights[4] + shuffleBallWeights[5]
    
    if side2 > side1{
        print("Right side heavier")
        print("\(shuffleBalls[3]) <-> \(shuffleBalls[4])")
        if shuffleBallWeights[4] > shuffleBallWeights[3]{
            print("Your ball is number \(shuffleBalls[4]) and it is heavier")
        } else if shuffleBallWeights[4] < shuffleBallWeights[3] {
            print("Your ball is number \(shuffleBalls[3]) and it is heavier")
        } else if shuffleBallWeights[4] == shuffleBallWeights[3] {
            print("Your ball is number \(shuffleBalls[5]) and it is heavier")
        }
    
    } else if side2 < side1 {
        print("Left side heavier")
        print("Not possible!!!")
    
    } else if side2 == side1 {
        print("Sides equal")
        print("\(shuffleBalls[0]) <-> \(shuffleBalls[1])")
        if shuffleBallWeights[1] > shuffleBallWeights[0] {
            print("Your ball is number \(shuffleBalls[0]) and it is lighter")
        } else if shuffleBallWeights[1] < shuffleBallWeights[0] {
            print("Your ball is number \(shuffleBalls[1]) and it is lighter")
        } else if shuffleBallWeights[1] == shuffleBallWeights[0] {
            print("Your ball is number \(shuffleBalls[2]) and it is lighter")
        }
        
    }
    
} else if side2 < side1 {
    print("Left side heavier")
    print("\(shuffleBalls[6]), \(shuffleBalls[7]), \(shuffleBalls[8]) <-> \(shuffleBalls[3]), \(shuffleBalls[4]), \(shuffleBalls[5])")

    side1 = shuffleBallWeights[6] + shuffleBallWeights[7] + shuffleBallWeights[8]
    side2 = shuffleBallWeights[3] + shuffleBallWeights[4] + shuffleBallWeights[5]
    
    if side2 > side1 {
        print("Right side heavier")
        print("Not possible!!!")
    
    } else if side2 < side1 {
        print("Left side heavier")
        print("\(shuffleBalls[3]) <-> \(shuffleBalls[4])")
        
        if shuffleBallWeights[4] > shuffleBallWeights[3]{
            print("Your ball is number \(shuffleBalls[3]) and it is lighter")
        } else if shuffleBallWeights[4] < shuffleBallWeights[3] {
            print("Your ball is number \(shuffleBalls[4]) and it is lighter")
        } else if shuffleBallWeights[4] == shuffleBallWeights[3] {
            print("Your ball is number \(shuffleBalls[5]) and it is lighter")
        }
    
    } else if side2 == side1 {
            print("Sides equal")
            print("\(shuffleBalls[0]) <-> \(shuffleBalls[1])")
        if shuffleBallWeights[1] > shuffleBallWeights[0]{
            print("Your ball is number \(shuffleBalls[1]) and it is heavier")
        } else if shuffleBallWeights[1] < shuffleBallWeights[0]{
            print("Your ball is number \(shuffleBalls[0]) and it is heavier")
        } else if shuffleBallWeights[1] == shuffleBallWeights[0] {
            print("Your ball is number \(shuffleBalls[2]) and it is heavier")
        }
    }
    
    
} else if side2 == side1 {
    print("equal")
    
    print("\(shuffleBalls[0]), \(shuffleBalls[1]), \(shuffleBalls[2]) <-> \(shuffleBalls[6]), \(shuffleBalls[7]), \(shuffleBalls[8])")
    side1 = shuffleBallWeights[0] + shuffleBallWeights[1] + shuffleBallWeights[2]
    side2 = shuffleBallWeights[6] + shuffleBallWeights[7] + shuffleBallWeights[8]
    
    if side2 > side1 {
        print("Right side heavier")
        print("\(shuffleBalls[6]) <-> \(shuffleBalls[7])")
        
        if shuffleBallWeights[7] > shuffleBallWeights[6] {
            print("Your ball is number \(shuffleBalls[7]) and it is heavier")
        } else if shuffleBallWeights[7] < shuffleBallWeights[6] {
            print("Your ball is number \(shuffleBalls[6]) and it is heavier")
        } else if shuffleBallWeights[7] == shuffleBallWeights[6] {
            print("Your ball is number \(shuffleBalls[8]) and it is heavier")
        }
    
    
    } else if side2 < side1 {
        print("Left side heavier")
        print("\(shuffleBalls[6]) <-> \(shuffleBalls[7])")
        
        if shuffleBallWeights[7] > shuffleBallWeights[6] {
            print("Your ball is number \(shuffleBalls[6]) and it is lighter")
        } else if shuffleBallWeights[7] < shuffleBallWeights[6] {
            print("Your ball is number \(shuffleBalls[7]) and it is lighter")
        } else if shuffleBallWeights[7] == shuffleBallWeights[6] {
            print("Your ball is number \(shuffleBalls[8]) and it is lighter")
        }
    
    } else if side2 == side1 {
        print("Sides equal")
        print("\(shuffleBalls[0]) <-> \(shuffleBalls[9])")
        
        if shuffleBallWeights[9] > shuffleBallWeights[0] {
            print("Your ball is number \(shuffleBalls[9]) and it is heavier")
        
        } else if shuffleBallWeights[9] < shuffleBallWeights[0] {
            print("Your ball is number \(shuffleBalls[9]) and it is lighter")
        }
    }
}

