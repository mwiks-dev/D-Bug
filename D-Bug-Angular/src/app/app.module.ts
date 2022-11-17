import { NgModule } from "@angular/core";
import { BrowserModule } from "@angular/platform-browser";

import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { HomeComponent } from "./components/home/home.component";
import { NavigationComponent } from "./components/navigation/navigation.component";
import { ProfileToggleComponent } from "./components/profile-toggle/profile-toggle.component";
import { SearchComponent } from "./components/search/search.component";
import { QuestionsComponent } from "./components/questions/questions.component";
import { SidebarComponent } from "./components/sidebar/sidebar.component";
import { AllQuestionsComponent } from "./components/all-questions/all-questions.component";
import { RankedUserComponent } from "./components/ranked-user/ranked-user.component";
import { QuestionComponent } from "./components/question/question.component";

import { AuthModule } from "@auth0/auth0-angular";
import { environment } from "src/environments/environment";
import { LoginComponent } from "./components/login/login.component";
import { LogoutComponent } from './components/logout/logout.component';
import { ProfileComponent } from './components/profile/profile.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NavigationComponent,
    ProfileToggleComponent,
    SearchComponent,
    QuestionsComponent,
    SidebarComponent,
    AllQuestionsComponent,
    RankedUserComponent,
    QuestionComponent,
    LoginComponent,
    LogoutComponent,
    ProfileComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    AuthModule.forRoot({
      domain: environment.domain,
      clientId: environment.clientId,
    }),
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
