//
//  ViewController.swift
//  hackUCI
//
//  Created by Lorena Macias on 1/31/20.
//  Copyright © 2020 AWSStudent. All rights reserved.
//

import UIKit
import Foundation


class ViewController: UIViewController, UITableViewDataSource, UITableViewDelegate,  UISearchBarDelegate {
    

    @IBOutlet weak var tableView: UITableView!

    var repo = Repository()
    var myAllergies = [String]()

    var newItem = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //addItem()
        if let loadedAllergies = repo.load(key: "allergies"){
            myAllergies = loadedAllergies as! [String]
        }
        
        self.tableView.delegate = self
        self.tableView.dataSource = self
        self.tableView.reloadData()
        
        //place button
        button()
        
        //everytime someone swipes, it calls the swipeAction function
        let leftSwipe = UISwipeGestureRecognizer(target: self, action: #selector(swipeAction(swipe:)))
        leftSwipe.direction = UISwipeGestureRecognizer.Direction.left
        self.view.addGestureRecognizer(leftSwipe)
    }

    @objc func touchBtn(sender: UIButton!){
        performSegue(withIdentifier: "item", sender: self)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if (segue.identifier == "item") {
            let dest = segue.destination as! addItem
            dest.vc = self
        } else if (segue.identifier == "swipeLeft") {
            let dest = segue.destination as! scanVC
            dest.allergies = myAllergies
        }
    }
    
    @objc func doubleTapped(){
        print("double tapped")
    }
    
    func addItem(){
        if self.newItem != "" {
            myAllergies.append(newItem)
            repo.save(key:"allergies",value:myAllergies)
        }
    }
    
    func button(){
        //custom button that displays over the tableView
        var addItemBtn = UIButton(frame: CGRect(origin: CGPoint(x: self.view.frame.width / 2 + 95, y: self.view.frame.size.height - 130), size: CGSize(width: 70, height: 70)))
        addItemBtn.backgroundColor = UIColor.white
        addItemBtn.addTarget(self, action: #selector(touchBtn), for: .touchUpInside)
        addItemBtn.setTitleColor(.black, for: .normal)
        addItemBtn.setTitle("+", for: .normal)
        addItemBtn.titleLabel?.font = UIFont.boldSystemFont(ofSize: 30)
        addItemBtn.layer.cornerRadius = 35
        addItemBtn.clipsToBounds = true
        //add the button
        self.view.addSubview(addItemBtn)

    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return myAllergies.count
        }

    func tableView (_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell{
            let cell = tableView.dequeueReusableCell(withIdentifier: "cell")
            let item = myAllergies[indexPath.row]

            cell?.textLabel?.text = myAllergies[indexPath.row]
//        cell?.textLabel?.backgroundColor = UIColor.green 
        return cell!
    }
    
    func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == UITableViewCell.EditingStyle.delete {
            myAllergies.remove(at: indexPath.row)
            tableView.reloadData()
            repo.save(key:"allergies",value:myAllergies)
        }
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let tap = UITapGestureRecognizer(target: self, action: #selector(doubleTapped))
        tap.numberOfTapsRequired = 2
        view.addGestureRecognizer(tap)
        
    }
    
    
}

//extension UIColor {
//    public convenience init?(hex: String) {
//        let r, g, b, a: CGFloat
//
//        if hex.hasPrefix("#") {
//            let start = hex.index(hex.startIndex, offsetBy: 1)
//            let hexColor = String(hex[start...])
//
//            if hexColor.count == 8 {
//                let scanner = Scanner(string: hexColor)
//                var hexNumber: UInt64 = 0
//
//                if scanner.scanHexInt64(&hexNumber) {
//                    r = CGFloat((hexNumber & 0xff000000) >> 24) / 255
//                    g = CGFloat((hexNumber & 0x00ff0000) >> 16) / 255
//                    b = CGFloat((hexNumber & 0x0000ff00) >> 8) / 255
//                    a = CGFloat(hexNumber & 0x000000ff) / 255
//
//                    self.init(red: r, green: g, blue: b, alpha: a)
//                    return
//                }
//            }
//        }
//
//        return nil
//    }
//}



