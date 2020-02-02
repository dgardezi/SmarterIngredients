//
//  CustomTableViewTableViewCell.swift
//  hackUCI
//
//  Created by Lorena Macias on 2/1/20.
//  Copyright © 2020 AWSStudent. All rights reserved.
//

import UIKit

class CustomTableViewCell: UITableViewCell {

    @IBOutlet weak var trashImg: UIImageView!
    /*let singleTap = UITapGestureRecognizer(target: self, action: #selector(tapDetected))
    trashImg.isUserInteractionEnabled = true
    trashImg.addGestureRecognizer9singleTap)
    */
    
    @IBOutlet weak var titleLabel: UILabel!
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }
    
}
