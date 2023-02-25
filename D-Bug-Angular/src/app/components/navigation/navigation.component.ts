import { Component, OnInit } from "@angular/core";
import { AuthService } from "@auth0/auth0-angular";

@Component({
  selector: "app-navigation",
  templateUrl: "./navigation.component.html",
  styleUrls: ["./navigation.component.scss"],
})
export class NavigationComponent implements OnInit {
  user: any = null;
  constructor(public auth: AuthService) {}

  ngOnInit(): void {
    this.user = this.auth.getUser();
    console.log(this.user.picture);
  }
}
