from fastapi import APIRouter

from user.service import service

router = APIRouter()

@router.post("/login")
def login():
    print("...controller...login...")
    service.login()
    return

@router.post("/register")
def register():
    print("...controller....register...")
    service.register()
    return

@router.post("/profile")
def profile():
    print("...controller....profile...")
    service.profile()
    return

@router.post("/logout")
def logout():
    print("...controller....logout...")
    return