"""
Dgardn Database Schemas

Each Pydantic model represents a collection in MongoDB.
Collection name is the lowercase of the class name.

Examples:
- User -> "user"
- Organization -> "organization"

These schemas are used for validation in API routes.
"""
from typing import List, Optional, Literal
from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime

# Accounts
class User(BaseModel):
    email: str = Field(..., description="Email address")
    name: str = Field(..., description="Full name")
    account_type: Literal['user','organization'] = Field('user')
    avatar_url: Optional[HttpUrl] = None
    bio: Optional[str] = None

class Organization(BaseModel):
    owner_user_id: str = Field(..., description="Owner user id")
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    location: Optional[str] = None
    logo_url: Optional[HttpUrl] = None
    cover_url: Optional[HttpUrl] = None
    subscription_price: float = Field(0, ge=0)

class TeamMembership(BaseModel):
    user_id: str
    organization_id: str
    role: Literal['owner','admin','member'] = 'member'

class Subscription(BaseModel):
    user_id: str
    organization_id: str
    status: Literal['active','canceled','past_due'] = 'active'
    started_at: Optional[datetime] = None

# Content
class Post(BaseModel):
    organization_id: str
    title: str
    description: Optional[str] = None
    image_url: Optional[HttpUrl] = None
    category: Optional[str] = None
    published_at: Optional[datetime] = None

class Course(BaseModel):
    organization_id: str
    title: str
    description: Optional[str] = None
    thumbnail_url: Optional[HttpUrl] = None
    price: float = Field(0, ge=0)
    difficulty: Optional[Literal['beginner','intermediate','advanced']] = None
    duration_hours: Optional[int] = Field(None, ge=0)
    category: Optional[str] = None

class Event(BaseModel):
    organization_id: str
    title: str
    description: Optional[str] = None
    image_url: Optional[HttpUrl] = None
    date: Optional[datetime] = None
    time: Optional[str] = None
    location: Optional[str] = None
    price: float = Field(0, ge=0)
    online: bool = True
    capacity: Optional[int] = Field(None, ge=0)

class Job(BaseModel):
    organization_id: str
    title: str
    description: Optional[str] = None
    type: Literal['full-time','part-time','internship','freelance'] = 'full-time'
    location: Optional[str] = None
    remote: Optional[Literal['remote','on-site','hybrid']] = 'remote'
    salary_min: Optional[int] = Field(None, ge=0)
    salary_max: Optional[int] = Field(None, ge=0)

class Message(BaseModel):
    organization_id: str
    user_id: str
    content: str
    thread_id: Optional[str] = None

# Simple saved/bookmark items
class SavedItem(BaseModel):
    user_id: str
    item_id: str
    item_type: Literal['post','course','event','job']
