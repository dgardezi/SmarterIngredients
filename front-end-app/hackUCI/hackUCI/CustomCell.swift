//
//  CustomCell.swift
//  hackUCI
//
//  Created by Lorena Macias on 2/1/20.
//  Copyright © 2020 AWSStudent. All rights reserved.
//

import Foundation
import UIKit

class CustomCell: UITableViewCell{
    var title : String?
    var img : UIImage?
    
    var titleView : UITextView = {
        var textView = UITextView()
        textView.translatesAutoresizingMaskIntoConstraints = false
        return textView
    }()
    
    var imgView : UIImageView = {
        var imageView = UIImageView()
        imageView.translatesAutoresizingMaskIntoConstraints = false
        return imageView
    }()
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        self.addSubview(imgView)
        self.addSubview(titleView)
        
        imgView.leftAnchor.constraint(equalTo: self.rightAnchor).isActive = true
        imgView.topAnchor.constraint(equalTo: self.topAnchor).isActive = true
        imgView.bottomAnchor.constraint(equalTo: self.bottomAnchor).isActive = true
        imgView.widthAnchor.constraint(equalTo: self.heightAnchor).isActive = true
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
