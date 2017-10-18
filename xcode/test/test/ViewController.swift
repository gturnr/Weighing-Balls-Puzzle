//
//  ViewController.swift
//  test
//
//  Created by Guy Turner on 16/10/2017.
//  Copyright © 2017 Guy Turner. All rights reserved.
//

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


class ViewController: UIViewController {
    
    var side1:Int?
    var side2:Int?
    
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
    
    
    @IBOutlet weak var generatedBallTxt: UILabel!
    @IBOutlet weak var resultsTxt: UILabel!
    
    @IBAction func generateBall(_ sender: Any) {
        
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

